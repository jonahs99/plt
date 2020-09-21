(define rail-dia 2.35)
(define rail-h 5)
(define rail-w 6)
(define rail-space 30)

(define servo-w 22.9)
(define servo-h 12.1)
(define thick 6)

(define hole-space 15)
(define hole-dia 2.85)
(define hole-dist 4)
(define h 20)
(define w (+ rail-space rail-w))

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

(define rail-holder
  (rotate-x
    (extrude
      (difference
        (rectangle [(- w) 0] [(half rail-w) (+ hole-dist rail-dia)])
        (circle (half rail-dia) [0 hole-dist]))
      (- thick) thick)
    (/ pi 2)))

(define plate
  (difference
    (rect w (dbl hole-dist) 1)
    (symmetric-x
      (circle (half hole-dia) [(half hole-space) 0]))))

(define servo
  (difference
    (rect (+ servo-w 4) (+ servo-h 4) 2)
    (rect servo-w servo-h 0)))

(union
  (extrude plate 0 thick)
  (intersection
    (symmetric-x
      (move
        rail-holder
        [(half rail-space) 0 thick]))
      plate)
  (move
    (extrude servo 0 thick)
    [0 (+ (half servo-h) hole-dist) 0]))