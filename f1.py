
import nltk
from neo4j import GraphDatabase
g=GraphDatabase.driver("bolt://localhost:11002", auth=("neo4j", "123456"))
session=g.session()
f = open("C:\\Users\\hp\\Desktop\\out.txt", "r")
for x in f:
    li=x.split(' | ')
    # print(li)
    s=li[-1]
    if s[-1]=='\n':
        s=s[0:len(s)-1]
        li[-1]=s
    li[1]=li[1].replace(' ','_')
    for i in range(len(li)):
        li[i]=li[i].lower()

    #print("8888888888",li[1])
    #query_node1 = "CREATE (a:Subject {Name: '" + li[0] + "'})"
    tokens = nltk.word_tokenize(li[0])
    t1 = nltk.pos_tag(tokens)
    tokens = nltk.word_tokenize(li[2])
    t2=nltk.pos_tag(tokens)
    #print(li[0],li[2],t1,t2)
    ok1=0
    ok2=0
    pts=['NN','NNP']
    try:
        for i in t1:
            #print(i,end=' ')
            if i[1] in pts:
                ok1=1
        for i in t2:
            #print(i)
            if i[1] in pts:
                ok2=1
        print(t1,t2,ok1,ok2)
    except IndexError:
        print(t1,t2)
    if ok1==1 and ok2==1:
        #print(li)
        query_node1 = "MERGE (a:Subject {Name:'" + li[0] + "'})"
        # query_node2 = "CREATE (b:Object {Name:'" + li[1] + "'})"
        #query_node3 = "CREATE (c:Predicate {Name:'" + li[2] + "'})"
        query_node2 = "MERGE (c:Predicate {Name:'" + li[2] + "'})"
        query_relation="MATCH(a:Subject),(c:Predicate) WHERE a.Name='"+li[0] +"' AND c.Name='"+li[2]+"' "    + " CREATE(a)-[r:"+li[1]+"]->(c)"
        #print(query_node1,"---->",query_node2,"---->",query_relation)
        session.run(query_node1)
        session.run(query_node2)
        session.run(query_relation)
    #print(query_node1,query_node2,query_relation)
