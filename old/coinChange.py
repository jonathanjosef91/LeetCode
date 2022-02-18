class Solution:
    def coinChange(self, coins, amount):
        if not coins or amount < 0:
            return -1
        if amount == 0:
            return 0

        reminders = {}

        self.__BT(coins,amount,0,len(coins)-1,reminders,0)

        if 0 not in reminders:
            return -1
        return reminders[0]


    def __BT(self, coins, amount, currentAmout, index, reminders, currentCoins):
        if amount == currentAmout:
            if 0 not in reminders or currentCoins < reminders[0]:
                reminders[0] = currentCoins
            return

        reminder = amount - currentAmout

        if (reminder in reminders and reminders[reminder] < currentCoins) or \
                (0 in reminders and currentCoins >= reminders[0]):
            return

        if reminder not in reminders:
            reminders[reminder] = currentCoins
        else:
            reminders[reminder] = min(currentCoins, reminders[reminder])

        if index < 0:
            return

        tempSum = 0
        tempCoins = 0
        while (tempSum < reminder) or (tempCoins + currentCoins) < reminders[reminder]:
            self.__BT(coins,amount,currentAmout+tempSum,index-1,reminders,currentCoins+tempCoins)
            temp += coins[index]
            tempCoins += 1






sol = Solution()
coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins, amount))










class SolutionBT_TimeExceed(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1

        coins.sort()
        return self.__backTrackingSol(coins,amount,0,-1,len(coins)-1,0)

    def __backTrackingSol(self, coins, amount, tempAmount, minCoins, index, numOfCoins):
        if tempAmount > amount or index < 0 or minCoins == self.__chooseCoin(minCoins, numOfCoins):
            return minCoins
        if tempAmount == amount:
            return self.__chooseCoin(minCoins, numOfCoins)
        if index == 0:
            if (amount - tempAmount)%coins[0] == 0:
                return self.__chooseCoin(minCoins, numOfCoins+ (amount - tempAmount)//coins[0])


        return self.__chooseCoin(
            self.__backTrackingSol(coins, amount, tempAmount+coins[index], minCoins, index, numOfCoins+1),
            self.__backTrackingSol(coins, amount, tempAmount, minCoins, index-1, numOfCoins),
        )

    def __chooseCoin(self, coin1, coin2):
        if coin1 == -1:
            return coin2
        if coin2 == -1:
            return coin1
        return min(coin1,coin2)