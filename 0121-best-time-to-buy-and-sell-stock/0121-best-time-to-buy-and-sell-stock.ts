function maxProfit(prices: number[]): number {
    let mp = 0;
    let bought_price = prices[0];

    for (const today_price of prices.slice(1)) {
        if (bought_price > today_price) {
            bought_price = today_price;
        }
        mp = Math.max(mp, today_price - bought_price);
    }
    return mp;
};