/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
         toBe: (another) => {
            if (val === another) {
                return true;
            } else {
                 throw new Error("Not Equal");
            }
        },   // close toBe and add a comma

        notToBe: (another) => {
            if (val !== another) {
                return true;
            } else {
                throw new Error("Equal");
            }
        }
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */