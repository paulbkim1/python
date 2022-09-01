const str1 = "aaaabbcddd";
const expected1 = "a4bbcd3";
const expected1b = "a4b2cd3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

const str5 = "abbbbbbbbbbbbbbbbb"
const expected5 = "ab17"

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */


function encodeStr(str) {
    var returnstring = ''
    var emptystring = ''
    var counter = 0
    if (str.length < 2) {
        return str
    }
    for (var i = 0; i < str.length; i++) {
        if (emptystring.length == 0) {
            emptystring += str[i];
            counter += 1
        }
        else if (str[i] == str[i - 1]) {
            counter += 1
        }
        else if (str[i] != str[i - 1]) {
            returnstring += emptystring;
            returnstring += counter.toString();
            emptystring = ""
            counter = 0
        }
    }
    return returnstring
}

console.log(encodeStr(str1)) // Expected: a4bbcd3
console.log(encodeStr(str2)) // Expected: ""
console.log(encodeStr(str3)) // Expected: a
console.log(encodeStr(str4)) // Expected: bbcc
console.log(encodeStr(str5)) // Expected: ab17

const strA = "a3b2c1d3";
const expectedA = "aaabbcddd";

const strB = "a3b2c12d10";
const expectedB = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
//helpful built-ins : isNaN() .repeat() parseInt() 
function decodeStr(str) {
    //Your code here
}

console.log(decodeStr(strA)) // Expected: aaabbcddd
console.log(decodeStr(strB)) // Expected: aaabbccccccccccccdddddddddd