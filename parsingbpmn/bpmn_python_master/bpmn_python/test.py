from parsingbpmn.bpmn_python_master.bpmn_python import bpmn_diagram_rep as diagram
from parsingbpmn.bpmn_python_master.bpmn_python import bpmn_import_utils as utils
from parsingbpmn.bpmn_python_master.bpmn_python import bpmn_python_consts as consts

bpmn_graph = diagram.BpmnDiagramGraph()
bpmn_graph.load_diagram_from_xml_file(r"/Users/giacomodiguida/Downloads/prova3.bpmn")
edges = bpmn_graph.get_flows()

#bpmn_graph.add_flow_node_to_diagram("Activity_0e44ssw", "Task", "TestProva", None)
bpmn_graph.add_textAnnotation_to_diagram("Process_0gzphmm", "TestAnnot3", "TextAnnotation_0dpjutk")


# bpmn_graph.add_task_to_diagram("Activity_0e44s34","TestProva",None)
#bpmn_graph.add_sequence_flow_to_diagram("Process_0gzphmm","Activity_0e44ssw", "TextAnnotation_sfecRIQgx", "Flow_05d8ocu")
#bpmn_graph.add_dataObject_to_diagram("Process_0gzphmm", "TestDataObject", None)
bpmn_graph.add_Assocation_to_diagram("Process_0gzphmm", "Activity_0e44ssw","TextAnnotation_0dpjutk", None)

for e in edges:
    print(e)

bpmn_graph.export_xml_file(r"/Users/giacomodiguida/Documents/", "bpmn9.bpmn")

"""
for tuple in lista:
    for dizionario in tuple:
        if type(dizionario) is dict:
            if dizionario['type'].endswith("Task"):
                #print(dizionario['type'])
                print(dizionario)
"""
