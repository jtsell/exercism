(ns bob (:require [clojure.string :as str]))

(defn response-for [x]
  (let [s (str/replace x #"[\d,:\(\)\%\$\^\@\#\*]" "")]
    (cond
      ; All caps, with question mark.
      (and
       (str/ends-with? (str/trim s) "?")
       (= s (str/upper-case s))) "Calm down, I know what I'm doing!"

      ; Ends in a question mark.
      (str/ends-with? (str/trim s) "?") "Sure."

      ; All whitespace
      (str/blank? s) "Fine. Be that way!"

      ; All caps.
      (= s (str/upper-case s)) "Whoa, chill out!"

      ; Anything else.
      :else "Whatever.")))

(str/replace ":) ?" #"[\d,:\(\)\%\$\^\@\#\*]" "")
" ?"
(str/replace "1, 2, 3 GO!" #"[\d,:\(\)\%\$\^\@\#\*]" "")
"   GO!"
(str/replace "ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!" #"[\d,:\(\)\%\$\^\@\#\*]" "")
"ZOMG THE  ZOMBIES ARE COMING!!!!!"
(str/replace "4?" #"[\d,:\(\)\%\$\^\@\#\*]" "")
"?"
(str/replace "1, 2, 3" #"[\d,:\(\)\%\$\^\@\#\*]" "")
"  "
