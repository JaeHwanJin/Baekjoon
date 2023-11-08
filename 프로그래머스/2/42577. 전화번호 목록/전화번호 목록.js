function solution(phone_book) {
    const phoneBookMap = new Map();
    phone_book.sort((a,b)=>a.length - b.length)
    for (const phoneNumber of phone_book) {
        for (let i = 1; i < phoneNumber.length; i++) {
            const prefix = phoneNumber.slice(0, i);
            if (phoneBookMap.has(prefix)) {
                return false;
            }
        }
        phoneBookMap.set(phoneNumber, true);
    }
    
    return true;
}
