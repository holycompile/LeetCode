/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
   let a_ok, b_ok;
    let adding_zeroes = (num, diff) => {
        for (let i = 1; i <= diff; i++) {
            num = "0" + num;
        }
        return num;
    };
    let diff = Math.abs(a.length - b.length);

    if (diff !== 0) {

        if (a.length <= b.length) {
            a_ok = adding_zeroes(a, diff);
            b_ok = b;
        }
        else {
            a_ok = a;
            b_ok = adding_zeroes(b, diff);
        }

    }
    else {
        a_ok = a;
        b_ok = b;
    }

    console.log("Equal length:", a_ok, b_ok);

    let binaryAdditonRule = (value1, value2) => {

        if (value1 === "0" && value2 === "0") {
            return "0";
        }

        else if (
            (value1 === "0" && value2 === "1") ||
            (value1 === "1" && value2 === "0")
        ) {
            return "1";
        }

        else if (value1 === "1" && value2 === "1") {
            return "exception";
        }
    };


    let finalized = "";
    let carry = "0";

    for (let i = a_ok.length - 1; i >= 0; i--) {

        let value1 = a_ok[i];
        let value2 = b_ok[i];

        let output = binaryAdditonRule(value1, value2);

        if (output === "exception") {

            if (carry === "1") {
                finalized += "1";
                carry = "1";
            }
            else {
                finalized += "0";
                carry = "1";
            }
        }

        else {

            if (carry === "1") {

                if (output === "0") {
                    finalized += "1";
                    carry = "0";
                }

                else if (output === "1") {
                    finalized += "0";
                    carry = "1";
                }
            }

            else {
                finalized += output;
            }
        }
    }

    if (carry === "1") {
        finalized += "1";
    }

    finalized = finalized.split("").reverse().join("");

    return finalized;
};