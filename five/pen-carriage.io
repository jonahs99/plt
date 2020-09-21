(define rail-space 30)
(define bush-dia 7.1)

(define v-space 28)
(define bush-h 4)
(define thick 2)

(define hole-dia 3)
(define hole-space 15)

(set-bounds! [-100 -100 -100] [100 100 100])
(set-quality! 8)
(set-resolution! 10)

(define (half a) (/ a 2))
(define (dbl a) (* a 2))
(define (rect w h r)
  (let
    ((hw (half w))
    (hh (half h)))
    (rounded-rectangle [(- hw) (- hh)] [hw hh] r)))

(define w (+ rail-space (dbl bush-dia)))
(define h (+ v-space (dbl bush-h)))

(define plate
  (intersection
    (symmetric-x (symmetric-y
      (union
        (box [0 0 0] [(half w) (half h) thick])
        (box [0 (- (half h) bush-h) thick] [(half w) (half h) (+ thick (* 1.4 bush-h))]))))
    (rect w h 2)))

(define bush
  (move
    (rotate-x
      (cylinder (half bush-dia) bush-h)
      (/ pi 2))
    [(half rail-space) (half h) (+ thick bush-h)]))

(define hole
  (circle (half hole-dia) [(half hole-space) (half hole-space)]))

(difference plate
  (symmetric-x (symmetric-y hole))
  (union
    bush
    (reflect-y bush)
    (reflect-x (reflect-y bush))))