class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        from collections import deque
        
        
        if endWord not in wordList:
            return 0
        
        
        
        dic ={}
        
        for word in wordList:
            for index in range(len(word)):
                temp = word[:index] +'*' +word[index+1:]
                
                if temp not in dic:
                    dic[temp] =[word]
                    
                else:
                    dic[temp].append(word)
                    
        for index in range(len(beginWord)):
                temp = beginWord[:index] +'*' +beginWord[index+1:]
                
                if temp not in  dic:
                    dic[temp] =[beginWord]
                    
                else:
                    dic[temp].append(beginWord)
                    
        visit = set([beginWord])
        count = 1 
        track = deque()
        track.append(beginWord)
        
        while track:
            
             
            
            for e in range(len(track)):
                word = track.popleft()
                
                if word == endWord:
                    return count 
                for index in range(len(word)):
                    temp = word[:index] +'*' +word[index+1:]
                    for wor  in dic[temp]:
                        if wor not in visit:
                            visit.add(wor)
                            track.append(wor)
            count+=1
          
        return 0
            
        
        
                
        
        
                    
            
            
            
            
                    
                
            