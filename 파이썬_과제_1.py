file = open('article.txt', 'w') # 작성
file.write('Senior officials at Ethiopia’s Ministry of Mines and Petroleum say the government is set to rescind an agreement with a US-based self-described energy firm after an investigation by Quartz Africa revealed the company had no petroleum industry expertise or technical credentials. After the story was published, one local social media user drove to the company’s listed address in Virginia, and found empty office space, with no sign of an extraction company in the area. When probed about the agreement earlier this year, Ethiopia’s minister of Mines Takele Uma told Quartz Africa he was unaware of GreenComm’s existence, saying he had “no clue.” His predecessor, Samuel Urkato, who has since gone on to become Ethiopia’s minister of Science and Higher Education, acknowledged the existence of the deal when reached by phone, but refused to speak any further, hanging up and ending the call. Zecharias Zelalem brings you the latest on the Ethiopian oil scandal.')
file.close()

with open('article.txt', 'r') as file:
    for line in file:
        words=line.split()
        wordcnt={}

        for word in words:
             if word in wordcnt:
                 wordcnt[word] += 1
             else:
                wordcnt[word]=1
        sorted_words = sorted([(k, v) for k, v in wordcnt.items()], key=lambda wordcnt: -wordcnt[1])
        for i in range(3):
            print(sorted_words[i])