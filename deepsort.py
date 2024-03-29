import numpy as np
import paddlex as pdx
from model import Embedding
from deep_sort import NearestNeighborDistanceMetric, Detection, Tracker

__all__ = ['DeepSort']


class DeepSort(object):
    def __init__(
            self,
            det_model_dir,
            emb_model_dir,
            use_gpu=False,
            threshold=0.5,
            max_cosine_distance=0.2,
            nn_budget=100,
            max_iou_distance=0.9,
            max_age=900,
            n_init=3
    ):
        self.detector = pdx.load_model(det_model_dir)
        self.emb = Embedding(emb_model_dir, use_gpu)
        self.threshold = threshold
        metric = NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
        self.tracker = Tracker(metric, max_iou_distance=max_iou_distance, max_age=max_age, n_init=n_init)

    def update(self, ori_img, threshold):
        self.height, self.width = ori_img.shape[:2]
        results = self.detector.predict(ori_img)
        tlwh = []
        xyxy = []
        confidences = []
        confid = 0.
        cnt = 0
        for result in results:
            if(result['score']) < threshold:
                continue
            x1, x2, w, h = result['bbox']
            tlwh.append([x1, x2, w, h])
            xyxy.append([x1, x2, x1 + w, x2 + h])
            confidences.append(result['score'])
            confid += result['score']
            cnt += 1


        tlwh = np.array(tlwh).astype(np.int)
        xyxy = np.array(xyxy).astype(np.int)
        confidences = np.array(confidences).astype(np.float)
        # generate detections
        if  len(tlwh) != 0:
            features = self.get_features(xyxy, ori_img)
            detections = [Detection(tlwh[i], conf, features[i]) for i, conf in enumerate(confidences)]

            # update tracker
            self.tracker.predict()
            self.tracker.update(detections)

            # output bbox identities
            outputs = []
            for track in self.tracker.tracks:
                if not track.is_confirmed() or track.time_since_update > 1:
                    continue
                box = track.to_tlbr()
                x1, y1, x2, y2 = box
                track_id = track.track_id
                outputs.append(np.array([x1, y1, x2, y2, track_id], dtype=np.float))


            if len(outputs) > 0:
                outputs = np.stack(outputs, axis=0)

            if cnt == 0:
                confid = 0
            else:
                confid /= cnt
            return outputs,confid

        else:
            return [],0

    def get_features(self, xyxy, ori_img):
        crops = []
        for bbox in xyxy:
            crop = ori_img[bbox[1]:bbox[3], bbox[0]:bbox[2], :]
            crops.append(crop)
        features = self.emb.predict(crops)
        return features


if __name__ == '__main__':

    deepsort = DeepSort('./model/detection', './model/embedding', True)
    import cv2

    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        success, frame = cap.read()
        outputs = deepsort.update(frame)
        if outputs is not None:
            for output in outputs:
                cv2.rectangle(frame, (output[0], output[1]), (output[2], output[3]), (0, 0, 255), 2)
                cv2.putText(frame, str(output[-1]), (output[0], output[1]), font, 1.2, (255, 255, 255), 2)
        print(outputs)
        cv2.imshow('test', frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
