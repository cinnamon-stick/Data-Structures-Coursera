(define fibonacci (lambda (number) 
  (cond [(<= number 1) number]
  [else (+ (fibonacci (- number 1 )) (fibonacci (- number 2)))]
  )
))
