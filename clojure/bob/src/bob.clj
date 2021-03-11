(ns bob (:require [clojure.string :as str]))

(defn question? [s] ; Ends in a question mark.
  (str/ends-with? (str/trim s) "?"))
   
  

(defn yelling? [s]
  (and
   (not (str/blank? (str/replace s #"[\W]" "")))
   (= s (str/upper-case s))))

(defn response-for [s]
  (cond
    (and (question? s) (yelling? s)) "Calm down, I know what I'm doing!"
    (question? s) "Sure."
    (str/blank? s) "Fine. Be that way!"
    (yelling? s) "Whoa, chill out!"
    :else "Whatever."))

; (let [s (str/replace x #"[\d,:\(\)\%\$\^\@\#\*]" "")])

(defn enblanken [s]
  (str/replace s #"[\W]" ""))

(enblanken ":) ?")
(enblanken "ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!")
(enblanken "4?")
(enblanken "1, 2, 3")
(enblanken "1, 2, 3 GO!")
