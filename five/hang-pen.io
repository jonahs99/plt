(set-bounds! [-50 -50 -10] [50 50 10])
(set-quality! 8)
(set-resolution! 10)

;; model parameters
(define line-spacing 40)
(define line-angle 90)
(define thickness 2)
(define chop 8)
(define float 2)

(define pen-dia 8)
(define pen-angle 35)
;;

(define (deg rad) (/ (* rad pi) 180))

(define half-spacing (/ line-spacing 2))
(define half-line-angle (/ line-angle 2))

(define height
  (/ half-spacing
    (tan (deg half-line-angle))))

(define pen-angle-sup
  (deg (- pen-angle 90)))

(define body
  (move
    (difference
      (symmetric-x
        (extrude
          (triangle [0 0] [half-spacing height] [0 height])
            0 thickness))
      (half-space [0 1 0] [0 chop 0]))
    [0 0 float]))

(define pen-support
  (rotate
    (box [-8 0 -2] [8 0 2])
    pen-angle-sup))

(define pen
  (rotate-x
      (cylinder (/ pen-dia 2) (* height 2))
      pen-angle-sup))

(difference body pen)