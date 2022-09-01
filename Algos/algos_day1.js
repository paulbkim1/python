str1 = "creature"
expected1 = ""
function reversestring(str)
for (i = str1.length - 1; i >= 0; i--) {
    expected1 += (str1[i])
}

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str1) {
    reversestring = "";
    for (i = str1.length - 1; i >= 0; i--) {
        reverseString += str1[i]
    }
}

//TEST CODE FOR REVERSE
console.log(reverseString(str1)) // Expected: erutaerc
console.log(reverseString(str2)) // Expected: god
console.log(reverseString(str3)) // Expected: olleh
console.log(reverseString(str4)) // Expected: ""