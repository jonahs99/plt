(set-bounds! #[-100 -100 -100] #[100 100 100])

(define screw_rad 2.8)
(define w 12)
(define l 30)
(define t 3)
(define pl 30)
(define pt 6)
(define pr 5.5)
(define angle 45)

(define pi 3.14159)
(define deg
  (lambda (d) (* (/ d 180) pi)))

(define cylinder-x
  (lambda (r h)
    (rotate-y
      (cylinder-z r h #[0 0 (- (/ h 2))])
      (deg 90))))

(move
(difference
  (cube #[(- (/ w 2)) (- (/ w 2)) (- (/ t 2))] #[(/ w 2) l (/ t 2)])
  (cylinder screw_rad t #[0 0 (- (/ t 2))]))
  #[0 (- l) 0])

(rotate-x
  (difference
    (union
      (cube #[(- (/ w 2)) 0 (- (- pt (/ t 2)))] #[(/ w 2) pl (/ t 2)])
      (cylinder-x (/ t 2) w))
      (move
        (rotate-x (cylinder-z pr (* 2 l) #[0 0 (- (/ l 2))]) (deg 270))
        #[0 0 (- (+ pr (/ t 2)))]))
  (deg angle))cube