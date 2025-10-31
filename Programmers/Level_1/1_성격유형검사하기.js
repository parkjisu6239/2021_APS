function solution(survey, choices) {
    let answer = '';
    
    const result = {
        R: 0,
        T: 0,
        C: 0,
        F: 0,
        J: 0,
        M: 0,
        A: 0,
        N: 0,
    }
    
    for(i=0; i<survey.length; i++) {
        const char = survey[i];
        const choice = choices[i];
        
        if (choice > 4) {
            result[char[0]] += 4 - choice;
        } else {
            result[char[1]] += choice - 4;
        }
    }
    
    ['RT', 'CF', 'JM', 'AN'].forEach(char => {
        const [a, b] = char;
        
        if (result[a] < result[b]) {
            answer += b;
        } else {
            answer += a;
        }
    })
    
    return answer;
}
