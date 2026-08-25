/** 
 * @param {string} str1 
 * @param {string} str2 
 * @return {string} 
 */ 

var gcdOfStrings = function(str1, str2) { 

    // First checking by adding them once
    let output = ""; 
    let added_string_1 = str1 + str2; 
    let added_string_2 = str2 + str1; 

    // If they don't have the same repeating pattern
    if (added_string_1 !== added_string_2) { 
        return ""; 
    } 

    // Now calculating the simple GCD
    let len1 = str1.length; 
    let len2 = str2.length; 

    // Calculating the GCD of len1 and len2
    const GCD = (len1, len2) => { 

        if (len1 == 0 || len2 == 0) { 
            return Math.max(len1, len2); 
        } 
        else { 

            // Find minimum of len1 and len2
            let result = Math.min(len1, len2); 

            while (result > 0) { 

                if (len1 % result == 0 && len2 % result == 0) { 
                    break; 
                } 

                result--; 
            } 

            // Return GCD
            return result; 
        } 
    } 

    // Now the GCD has the value
    let gcd = GCD(len1, len2); 

    // Take the first 'gcd' characters from str1
    for (let i = 0; i < gcd; i++) { 
        output += str1.charAt(i); 
    } 

    return output; 
};