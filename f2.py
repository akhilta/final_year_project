from neo4j import GraphDatabase
#
# class HelloWorldExample(object):
#
#     def __init__(self, uri, user, password):
#         self._driver = GraphDatabase.driver(uri, auth=(user, password))
#
#     def close(self):
#         self._driver.close()
#
#     def print_greeting(self, message):
#         with self._driver.session() as session:
#             greeting = session.write_transaction(self._create_and_return_greeting, message)
#             print(greeting)
#
#     @staticmethod
#     def _create_and_return_greeting(tx, message):
#         result = tx.run("CREATE (a:Greeting) "
#                         "SET a.message = $message "
#                         "RETURN a.message + ', from node ' + id(a)", message=message)
#         return result.single()[0]
#
# #h1=HelloWorldExample("bolt://localhost:7687","neo4j","123456789")
g=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "123456"))
session=g.session()
li=[["Photosynthesis","is_an","endergonic process."],["Photosynthesis","is_an","exogenic process."],["Photosynthesis","is_an","isogenic process."] ,["Photosynthesis","is_an"," Normal process."]]
ans=['A','B','C','D']
for i in range(4):
    q1='MATCH(b:Subject) - [r:'+li[i][1]+'] -> (u:Predicate) WHERE b.Name="'+li[i][0]+'" And u.Name="'+li[i][2]+'" return b,r,u;'
    nodes=session.run(q1)
    for node in nodes:
        print('Answer for this question is option ' ,ans[i])


