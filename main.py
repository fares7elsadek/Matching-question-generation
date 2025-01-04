from app.Model import MatchingQuestions
import random
from prettytable import PrettyTable
from IPython.display import Markdown, display

text = """Process scheduling is a fundamental concept in operating systems that ensures efficient utilization of the CPU by managing the execution of multiple
processes. In a multitasking environment, the CPU must allocate its time among various processes, balancing responsiveness, throughput, and fairness.
The operating system achieves this through a scheduler, which determines the order in which processes are executed based on predefined algorithms.
There are three primary types of process schedulers: Long-term scheduler, Short-term scheduler, and Medium-term scheduler. The long-term scheduler
selects processes from the job queue and loads them into the ready queue, controlling the degree of multiprogramming. The short-term scheduler, also
known as the CPU scheduler, decides which process gets the CPU next and for how long. Lastly, the medium-term scheduler temporarily removes processes
from memory to reduce the load and improve system performance, a process known as swapping.  Scheduling algorithms, such as First-Come, First-Served
(FCFS), Shortest Job Next (SJN), Round Robin (RR), and Priority Scheduling, define how processes are prioritized. For instance, Round Robin ensures
fairness by allocating a fixed time slice to each process, while Priority Scheduling executes processes based on their assigned priority.  Efficient
process scheduling reduces CPU idle time, minimizes waiting time, and ensures that high-priority tasks are completed promptly. It plays a crucial role
in maintaining system stability and ensuring optimal performance across diverse computing environments."""



def printmd(string):
    display(Markdown(string))



model = MatchingQuestions(text)
keywordBestSense = model.get_matching_questions()


x = PrettyTable()
all_keywords= list(keywordBestSense.keys())
all_definitions = list(keywordBestSense.values())
random.shuffle(all_keywords)
random.shuffle(all_definitions)


x.field_names=['Word', "Definition"]
for word,defn in zip(all_keywords,all_definitions):
  x.add_row([word,defn])

printmd("**Match the following words to their correct meanings.**")

print (x)