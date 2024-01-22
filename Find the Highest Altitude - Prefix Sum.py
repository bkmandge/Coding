"""
                        Find the Highest Altitude

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
"""


def findHighestAltitude(gain):
    # initialise altitude sum and highest altitude to 0
    alt_sum = 0
    highest_alt = 0

    # loop through entire gain list
    for i in range(len(gain)):
        # calculate total altitude & compare highest altitude at each point & return highest altitude
        alt_sum = alt_sum + gain[i]
        highest_alt = max(highest_alt, alt_sum)
    return highest_alt


# gain = [-5,1,5,0,-7]

gain = [-4,-3,-2,-1,4,3,2]

print(findHighestAltitude(gain))

