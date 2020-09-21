(set-bounds! [-100 -100 -100] [100 100 100])
(set-quality! 8)
(set-resolution! 10)

; params
(define spacing 15)
(define dia 3.5)
(define thickness 2)
(define h 8)
(define pen-dia 13)
(define pen-angle 45)
(define groove 2)

(define (half a) (/ a 2))
(define (dbl a) (* a 2))
(define (rect w h r)
  (let
    ((hw (half w))
    (hh (half h)))
    (rounded-rectangle [(- hw) (- hh)] [hw hh] r)))

(define w (+ spacing (* 2 dia)))
(define plate
  (extrude
    (difference
      (rect w w 2)
      (symmetric-x (symmetric-y
        (circle (half dia) [(half spacing) (half spacing)]))))
    0 h))

(define center [(- w dia) (- h dia) 0])
(define plate2
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

(define pen-profile
  (union
    (move
      (rotate (rectangle-centered-exact [(/ pen-dia (sqrt 2)) (/ pen-dia (sqrt 2))]) (/ pi 4))
      ;(circle (half pen-dia))
      [0 (+ (half pen-dia) thickness)])
    (symmetric-x
      (rectangle-centered-exact [groove (dbl groove)] [(half pen-dia) 0]))))
(define pen
  (rotate-z
    (rotate-x
      pen-profile (/ pi 2))
    (* pi (/ pen-angle 180))))

(difference
  plate
  pen)