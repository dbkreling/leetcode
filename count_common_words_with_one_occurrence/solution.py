#!/usr/bin/python

#words1, words2 = ["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]
# words1, words2 = ["b","bb","bbb"],["a","aa","aaa"]
# words1, words2 = ["a","ab"], ["a","a","a","ab"]
words1 = ["bjxzvssdoq","oom","lxrrvf","aoeselhvrnw","awnornqyztqlza","bjxqkapuvaw","wibxruerngdzgjd","rezrwdzvllpbjpnikhzraz","pswmnrsepudx","nlicjldpeia","glg","nllxfcjjitmsuugmr","cl","pysmpgjakkjnusfopphb","zxlwcdjpn","xktsfnchwrdesnf","qptnoxxgrjmvr","exlfwjfsbsirbbkyqjtinrrwuhh","rqbnghajxygilgdjejopyuwyjqrx","vrjkqsicuqoalqyaxkaaogxbf","ixnlltqbpygmpjuspom","izajsxotcbhzdnkujwgdzo","b","lighabre","i","ljqqbfddipvcooh","hboedpepeeunx","bkhzhiefammwqkhvampokd","ptlozguwmyyp","loeshsjgazzwvs","kyrltbdzlymjxtvwiiq","fk","mbjpgwsahkgkehlcoqbhunqchxj","nfyuvlrmiturheb","cyqwsiysmoirurj","sciqruywy","podsrhmsozan","nlyadkrxhdbup","gdugldwghzt","wpjm","gjobdekmjisjgadkwwemnmco","dkjdtimdghvlhuetxyaklk","iwqylhdwqbwaqdouowoodhs","mn"]
words2=["eeormvovhzslwsqgzthlgntgzc","zfwownznh","suxrkdbjdjjtbkjucsbyk","u","y","lbjooktoctgwbbptiffytquha","dcsxrghgpultkatbecjadbespvww","vwduylshcpaiu","rtcxwctvquaiuwkgvdx","a","szearxmdqcismljmihbtkcirztdnrc","htgmuxtxdunsvfizb","hybe","nsegkgwcvopncmfpaahhhjeuqjosv","jtarnnpppxtzmopixeijqqahkd","hazcgrrnpourkyoeanodejiptne","kurhokvhixihe","ljwycewmecfqdhtxiokjn","qgjzzvpyvwetlsvcsw","aunns","nwcnfrzzvxafkfjfnczummtubikji","nipiygnvlfntgpxfedj","mgnt","xvjehufvaqouhztnmts","sjtbrfjwtqxakqktxjaljrbwfoxvz","dfeujeikfrtrpiafrgxvjlkpxtog","u","ggbcxoasodaqaazulrxjleecexey","inedrgssajhpygfvozigohis","pevxwgfzxebybfe","cgy","fnhvlx","vxfybaebkoq","xvhx","mxbqjtanctljewwjjlbpkgbtsm","mlwagamcikbcpuexhikmizp","qeiomipvsoqlsnhylulirrcwtqga","bwemqcgyusuauwlpbjjru","iimcbidtndh","lpjejlkmxtlbyvnscy","dlspriicnyykdsyvswlgktavwloq","dib","qoptbduulgqwquvhdvmwdz","xrtxghrbfrhpzduxeljnctgg","schmbsaupayqnpchn","kah","itotymryqufqpozrwmvsl","gurb","xsyocxcmwvqmnmxthfemmu","pkfdutm","hkbwxwjxyuld","ukdqszfjckdunnhpevw","kqfwytdvnvjrchiwprcqkfntqticsc","zjmsfwjddgjiypsmagdrujb","gn","ebncbjvhpbjecbrizdpv","nbfehcktwswih","sttmqcdmobdgtgkyxydyovahknjbsn","sryyufrtocf","eiicpwknxrzqylqpybhfd","pey","njimttradeoa","wcogjdfr","prva","tyxdmxgw","wluzocppg","kzm","wbyyperlkflaoxyxftzwxvmemof","snzpclbulddnmmjmpdurcybo","mowxgpmzojtmympmt","uvtnojjahrovzmlukf","sykhtgejlmbzshhneoyqr","ib","haqkkizidifykwijm","csjtexnr","yvgr","vzcxbtlthrynnawxnkxdptp","yvxrmscsckv"]


# My Solution: This solution is wrong if the same list contains the same word twice.
# merged = []
# unique_dups = []

# answer = 0

# words1.extend(words2)

# merged = words1

# for i in merged:
#     count = merged.count(i)
#     if count == 2:
#         answer += 1
#         unique_dups.append(i)

# print(int(answer/2), ":", merged)
# print("Unique duplicates are:", set(unique_dups))


# Alternative solution
answer = 0
unique_dups = []

for i in words1:
    if words1.count(i) == 1 and words2.count(i) == 1:
        answer += 1
        unique_dups.append(i)

print("Answer:", answer)
print("Unique duplicates are:", unique_dups)
