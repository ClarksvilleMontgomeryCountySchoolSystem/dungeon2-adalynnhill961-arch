good = r"""
                                     _ 
                                    | |
 _ __ __ _ _ __  _   _ _ __  _______| |
| '__/ _` | '_ \| | | | '_ \|_  / _ \ |
| | | (_| | |_) | |_| | | | |/ /  __/ |
|_|  \__,_| .__/ \__,_|_| |_/___\___|_|
          | |                          
          |_|  
"""
bad = r"""
   :o
    ~  $r
   4% n$$
   '!!!MR
   '!!X!!
    !!!X
   
'!!!    `!!!
 `!~     !!~

    Moon Knight
"""


drawbridge_raised = True
if not drawbridge_raised:
    outcome = "Thunder: Wow boom its loud."
    print(good)
else:
    outcome = "Doom: It's nice today."
    print(bad)
print(outcome)