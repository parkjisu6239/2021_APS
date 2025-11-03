function solution(users, emoticons) {
    var answer = [0, 0];
    
    const discount = [10, 20, 30, 40];
    const combi = [];
    
    const combination = (discountEmoticons) => {
        if (discountEmoticons.length === emoticons.length) {
            return combi.push(discountEmoticons)
        }
        
        discount.forEach((dis) => {
            combination([...discountEmoticons, dis])
        })
    }
    
    combination([]);
    
    combi.forEach((com) => {
        let plus = 0;
        let sales = 0;

        users.forEach(user => {
            let expense = 0;
            for(let i=0; i<com.length; i++) {
                if (com[i] >= user[0]) {
                    expense += emoticons[i] * ((100 - com[i]) / 100)
                }
                
                if (expense >= user[1]) {
                    break
                }
            }
            
            if (expense >= user[1]) {
                plus++
            } else {
                sales+=expense;
            }
        })
        if (plus > answer[0]) {
            answer = [plus, sales]
        } else if (plus >= answer[0] && sales > answer[1]) {
            answer = [plus, sales]
        }
    })
    return answer;
}
