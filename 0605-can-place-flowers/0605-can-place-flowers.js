/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {

    let counter = 0;
    let copy = [...flowerbed];

    for (let i = 0; i <= copy.length - 1; i++) {

        // Other positions
        if (i != 0 && i != copy.length - 1 && copy[i] === 0) {

            if (copy[i + 1] != 1 && copy[i - 1] != 1) {
                copy[i] = 1;
                counter++;
            }
        }

        // First position
        else if (i === 0 && copy[i] === 0) {

            if (copy[i + 1] != 1) {
                copy[i] = 1;
                counter++;
            }
        }

        // Last position
        else if (i === copy.length - 1 && copy[i] === 0) {

            if (copy[i - 1] != 1) {
                copy[i] = 1;
                counter++;
            }
        }
    }

    return counter >= n;
};