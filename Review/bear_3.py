def ArrayChallenge(strParam):
  answer = 0 # anagrams count

  words = list(set(strParam.split()))
  new_words = []
  for word in words:
    new_words.append("".join(sorted(word)))
  new_words_set = set(new_words)
  for nw in new_words_set:
    cnt = new_words.count(nw)
    if cnt > 1:
      answer += (cnt -1)

  return answer

# keep this function call here
print(ArrayChallenge(input()))