import pickle
with open("cur.dat", "rb") as fp:
    print(pickle.load(fp))
with open("cur.dat", "wb") as fp:
    k={'month': 11, 'idn': 0}
    pickle.dump(k, fp)

ci = ['f00ee90c-844e-429b-b0d8-e83b6b0f8485', '5942cc6e-8a9a-43e1-b08b-b6086b662d3e', 'a0b2bbc8-7bbc-4ff6-8297-bcf0274a59f7', 'acc0a85d-1da2-4e81-952f-1733aba6f6da', '31fd9e38-da94-4abe-9bd3-be994f2f3eb1', '73f05917-83b4-47ea-9f8e-b52cdc369f75', '3ca53c5f-7e04-4b30-9771-1f4c56e1486d', 'a34b103f-51bc-4dd0-a4af-f2ad389c6f5c', '2b7cb818-2538-4290-b3d4-c58ee7e6c207', 'd6f78a8a-5b71-43d9-98d0-39cddb82e2a2', 'e4f92bf6-13a8-4b16-9538-fe5bd19d137f', '82865ebc-5315-4b1b-a716-8bb1d0b1fdce', '55f26a6b-3e1b-4bcf-a9c1-2147e6884200', '48091455-2ab2-42db-ade6-6b628cf992f1', '25df754a-b4c7-4836-b188-7ff8c0a6f58c', '8e07c94a-843d-4050-95f7-ff83bcc1c891', 'f3c3b3cc-a44e-4f37-bc38-25cf1de6c15a', '31d15410-d02c-4184-aa1c-76535d38b6b4', 'f15908a9-ff66-453e-81d0-a7cc8c63c039']
cs = ['22ba986cc956b6b4fd2b75b818c5c83f', 'ae9b39c64b73e72ab8d7dad8b036213a', '9325c76d2e4335071c97219bc105181a', '54a726f034e76edbfc5748d2548eab8c', '33b434f56b041bf6a8276af805bb73bb', '87fbdf770caf7daf439e824c17bfd3a7', '3115daff089a9c33dcab910eca19a86b', '848ec34b02ee0fa40fd77a74ebcc9c73', 'c5c4c907263cb1ff79062d20dc99c5a0', '38591d60eb8e7c407c610c82a87f4d10', 'a6feb8e0782e5f7fb0fc2da57940312e', '6f083c1a83f5b3ca0c5eab2df95929a9', '5292223022389d951eafb09245ca3c3a', 'bc55be74d4ed10440e2f93fc768719e4', '8fbdf6c7cdbb32fe32e57409f708198b', 'c460ca6b13694b4c6569adacc3ca12d0', '642a08be16e482424f91e7cc988a9b9c', '63850efcb987e0c11c2b8064d5b87b49', 'cca5cfc06ecf9f598e8320b0971dee3d']

print(len(ci), len(cs))

# ci=[]
# cs=[]

# try:
#     fp=open("data.pkl", "rb")
#     while True:
#         k=pickle.load(fp)
#         ci.append(list(k.keys())[0])
#         cs.append(list(k.values())[0])
        
# except:
#     fp.close()

# print(ci, cs, sep="\n")




