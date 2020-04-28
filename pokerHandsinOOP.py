suits = 'CDHS'
ranks = '23456789TJQKA'

from abc import ABCMeta, abstractmethod

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """

    def __init__(self, rank_suit):
        if len(rank_suit) == 2:
            self.rank, self.suit = rank_suit
        elif len(rank_suit) == 3: 
            self.rank = rank_suit[:2]
            self.suit = rank_suit[2:]
        else:
            raise ValueError("{}: Illegal card".format(rank_suit))  
        self.card = rank_suit

    def __repr__(self):
        return self.card
    
    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()



class PKCard(Card):
    """Card for Poker game
    """
    def value(self) :
        values = dict(zip(ranks, range(2, 2 + len(ranks))))
        for i,j in values.items() :
            if self.card[0]==i :
                return j


if __name__ == '__main__':
    c1 = PKCard('QC')
    c2 = PKCard('9D')
    c3 = PKCard('9C')
    print(f'{c1} {c2} {c3}')
    # comparison
    print(c1 > c2 == c3)

    # sorting
    cards = [c1, c2, c3, PKCard('AS'), PKCard('2D')]
    sorted_cards = sorted(cards)
    print(sorted_cards)
    cards.sort()
    print(cards)


import random
class Deck():
    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.cards = [cls(r+s) for s in suits for r in ranks]
        self.rand = random.Random(113)

    def __str__(self) :
        return "{}".format(repr(self.cards))
    
    def __len__(self) :
        return len(self.cards)
    
    def __getitem__(self, index) :
        return self.cards[index]
    
    def shuffle(self) :
        self.rand.shuffle(self.cards)
    
    def pop(self) :
        if not self.cards: raise ValueError("No more cards!")
        return self.cards.pop()

if __name__ == '__main__':
    deck = Deck(PKCard)  # deck of poker cards
    deck.shuffle()
    c = deck[0]
    print('A deck of', c.__class__.__name__)
    print(deck)
    # testing __getitem__ method
    print(deck[-5:])

    while len(deck) >= 10:
        my_hand = []
        your_hand = []
        for i in range(5):
            for hand in (my_hand, your_hand):
                card = deck.pop()
                hand.append(card)
        my_hand.sort(reverse=True)
        your_hand.sort(reverse=True)
        print(my_hand, '>', your_hand, '?', my_hand > your_hand)


class Hands:
    
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        self.cards = sorted(cards, reverse=True)

    def flush(self) :
        cards = self.cards
        l = []
        for suit in cards :
            l.append(suit[1])
        if l.count(l[0]) == 5 :
            return True
        else :
            return False

    def straight_flush(self) :
        cards = self.cards
        if cards.flush() and cards.straight():
            return True
        else:
            return False

    def straight(self) :
        cards = self.cards
        values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}
        l = []
        for card in cards :
            for rank in values.keys() :
                if card[0] == rank :
                    l.append(values[rank])
        l.sort(reverse= True)
        if l == [14,5,4,3,2] :
            return None
        small = l[-1]
        ll = []
        for i in range(5) :
            ll.append(small)
            small += 1
        ll.sort(reverse=True)
        if l == ll :
            return self.cards
        else : 
            return False

    def classify_by_rank(self):
        rankdic = {}

        for i in ranks:
            l = []
            for card in self.cards:
                if card[0] == i:
                    l.append(card)
                rankdic[i] = l
        return rankdic
        
    def find_a_kind(self):
        cards_by_ranks = self.classify_by_rank()
        count1 = 0
        count2 = 0
        rank = 0
        card = []
        for key in cards_by_ranks.keys() :
            if len(cards_by_ranks[key]) == 2 :
                count1 += 1
            if len(cards_by_ranks[key]) == 3 :
                count2 += 1
            if len(cards_by_ranks[key]) == 4 :
                rank = 8
                return "four of kind"
        if count1==1 and count2 ==1 :
            rank = 7
            return "full house"
        elif count2 == 1 :
            rank = 4
            return "three of kind"
        elif count1 == 1 :
            rank = 1
            return "one pair"
        elif count1 == 2 :
            rank = 2
            return "two pair"
    
    def tell_hand_ranking(self):
        cards = self.cards
        countf = 0
        counts = 0
        countr = 0
        countb = 0
        if cards.is_flush()== True :
            countf += 1
            countr += 1
            countb += 1
        if cards.is_straight(cards) == True :
            cards.sort(reverse= True)
            if cards[0][0] == 'T' and cards[4][0]=='A':
                countr += 1
            elif cards[0][0] == 'A':
                countb += 1
            counts += 1
        if countr == 2 :
            return "royal straight flush"
        elif countb == 2 :
            return "back straight flush"
        elif countf == 1 and counts == 1 :
            return "straight flush"
        elif countf == 1 :
            return "flush"
        elif countb == 1 :
            return "back straight" 
        elif counts == 1 :
            return "straight"
        if cards.is_flush() == False and cards.is_straight()==False and cards.find_a_kind() == None :
            return "No pair"
        return cards.find_a_kind()

    def compare(self, other) :
        self.tell_hand_ranking()
        other.tell_hand_ranking()
        dic1 = zip(self.rank[0], other.rank[0])

        if self.rank[0] > other.rank[0] :
            return True
        elif self.rank[0] < other.rank[0] :
            return False
        else : 
            for i, j in dict1.items() :
                if i > j :
                    return True
                elif i < j :
                    return False

rank_name = ["No pair", "one pair", "two pair", "three of kind", "straight", "flush", "full house", "four of kind", "straight flush"]
rank_dict = dict(zip(range(9), rank_name))

if __name__ == '__main__':
    import sys
    def test(did_pass):
        """  Print the result of a test.  """
        linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)

    # deck = Deck(PKCard)
    # deck.shuffle()
    # test = []

    # test.append(Hands([PKCard('3D'), PKCard('2S'), PKCard('7S'), PKCard('3C'), PKCard('9S')]))
    # test.append(Hands([PKCard('3D'), PKCard('AS'), PKCard('7S'), PKCard('TC'), PKCard('TS')]))
   

    # test(test[0].compare(test[1]) == True)
    