(set-bounds! [-100 -100 -100] [100 100 100])
(set-quality! 8)
(set-resolution! 10)

(define bushing-dia 7.2)
(define bushing-height 15)
(define thickness 2)
(define spacing 35)

(define (dbl x) (* 2 x))
(define (half x) (/ x 2))

(define outer-dia (+ bushing-dia (dbl thickness)))

(symmetric-x
  (difference
    (union
      (box-mitred-centered [spacing outer-dia bushing-height])
      (cylinder (half outer-dia) bushing-height [(half spacing) 0 (- (half bushing-height))]))
    
      (cylinder (half bushing-dia) bushing-height [(half spacing) 0 (- (half bushing-height))])
      (rotate-x
        (cylinder 4 outer-dia [0 0 (- (half outer-dia))])
        (half pi))))

