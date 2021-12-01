(load "day-1-data.scm")

(define (count_depth_increases window readings)
  (cond ((= (length readings) window)
         0)
        ((< (calculate-window window readings)
            (calculate-window window (cdr readings)))
         (+ (count_depth_increases window (cdr readings)) 1))
        (else (count_depth_increases window (cdr readings)))))

(define (calculate-window n readings)
  (if (<= n 0)
      0
      (+ (car readings)
         (calculate-window (- n 1) (cdr readings)))))

(display (count_depth_increases 1 elf-readings))
(newline)
(display (count_depth_increases 3 elf-readings))
(newline)
