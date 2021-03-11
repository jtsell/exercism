(ns reverse-string)

(defn reverse-string [s]
  (apply str (reverse s))
)

(reverse-string "Hello")
(reverse-string "what") 
