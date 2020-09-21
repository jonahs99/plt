(set-bounds! [-100 -100 -100] [100 100 100])
(set-quality! 8)
(set-resolution! 10)

; params
(define spacing 15)
(define dia 3.5)
(define thread-dia 2.8)
(define thickness 2)
(define sq-width (+ 10.9 0.3))
(define sq-length (+ 11.1 0.3))
(define sq-height 12)
(define sq-thickness 1.6)

(define (half a) (/ a 2))
(define (dbl a) (* a 2))

(define w (/ (+ spacing (* 2 dia)) 2))
(define h w)
;(define h (half (+
;  (* 2 (sqrt 2) sq-thickness)
;  (sqrt (+ (* sq-width sq-width) (* sq-length sq-length))))))
(define center [(- w dia) (- h dia) 0])
(define plate
  (symmetric-x (symmetric-y
    (difference
      (box [0 0 0] [w h thickness])
      (difference
        (box [(- w dia) (- h dia) 0] [w h thickness])
        (move
          (cylinder dia thickness)
          center))
      (move
        (cylinder (half dia) (* 4 thickness) [0 0 (- thickness)])
          center)))))

(define (rect w h r)
  (let
    ((hw (half w))
    (hh (half h)))
    (rounded-rectangle [(- hw) (- hh)] [hw hh] r)))
(define square
  (rotate-z
    (move
      (difference
        (extrude
          (rect (+ sq-width (dbl sq-thickness)) (+ sq-length (dbl sq-thickness)) sq-thickness)
          (- (half sq-height)) (half sq-height))
        (box-mitred-centered [sq-width sq-length sq-height])
        (move
          (rotate-x
            (cylinder-z (half thread-dia) sq-length)
            (/ pi 2))
          [0 0 (/ sq-height 6)])
        (move
          (rotate-y
            (cylinder-z (half thread-dia) sq-length)
            (/ pi 2))
          [0 0 (- (/ sq-height 6))]))
      [0 0 (+ thickness (half sq-height))])
    (/ pi 4)))

(union plate square)
