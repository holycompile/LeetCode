var kidsWithCandies = function(candies, extraCandies) {
    // calculating the greatest of all the candies
    let greatest_candy = 0;

    for(let i = 0; i < candies.length; i++){
        if(candies[i] >= greatest_candy){
            greatest_candy = candies[i];
        }
    }

    let output = [];

    for(let i = 0; i < candies.length; i++){
        let added_candy = candies[i] + extraCandies;

        if(added_candy >= greatest_candy){
            output.push(true);
        }
        else{
            output.push(false);
        }
    }

    return output;
};