/* 
Given an int to represent how much change is needed
calculate the fewest number of coins needed to create that change,
using the standard US denominations
*/
// quarter = 25 cents, dime = 10, nickel = 5, penny = 1
const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * @param {number} cents
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
    //Your code here
}

console.log(fewestCoinChange(cents1)) // { quarter: 1 }
console.log(fewestCoinChange(cents2)) // { quarter: 2 }
console.log(fewestCoinChange(cents3)) // { nickel: 1, penny: 4 }
console.log(fewestCoinChange(cents4)) // { quarter: 3, dime: 2, penny: 4 }


// Solution

// function fewestCoinChange(cents) {
//     //Your code here
//     coins = {}
//     if( cents >= 25){
//         coins['quarter'] = Math.floor(cents/25)
//         cents = cents % 25
//     }
//     if( cents >= 10){
//         coins['dime'] = Math.floor(cents/10)
//         cents = cents % 10
//     }
//     if( cents >= 5){
//         coins['nickel'] = Math.floor(cents/5)
//         cents = cents % 5
//     }
//     if (cents >=1 ){
//         coins['penny'] = cents
//     } 
//     return coins
// }

    // OR

// function fewestCoinChange(cents) {
//     let coins = {'quarter': 0, 'dime': 0 , 'nickel': 0, 'penny' : 0 }

//     while (cents >= 25){
//         coins['quarter']++
//         cents -= 25

//     }
//     while (cents >= 10){
//         coins['dime']++
//         cents -= 10
//     }
//     while (cents >= 5){
//         coins['nickel']++
//         cents -=5
//     }
//     while (cents>= 1){
//         coins['penny']++
//         cents -=1
//     }
//     let filtered_coins = Object.keys(coins).filter(coin=>coins[coin] == 0)
//     // return filtered_coins
//     for (key of filtered_coins){
//         // console.log(key)
//         delete coins[key]
//     }
//     return coins
// }