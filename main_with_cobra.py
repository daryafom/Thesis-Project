import numpy as np
from cobra import Model, Reaction, Metabolite, io, core


class FBA:
    def __init__(self, path):
        """
        path: путь к файлу, в котором лежит модель
        загрузка модели с помощью io.load_json_model
        v1: значение целевой функции для исходного
        """

        self.model = io.load_json_model(theFileWithModel)
        self.v1 = self.model.optimize().objective_value

    def algoritm(self):
        """
        Алгоритм последовательного выключения генов (алгоритм зануления)
        return: возвращается список остановленных реакций и
        их влияние на изменение значения целевой функции (в процентах)
        """

        list_value_opt = []
        for gene in self.model.genes:
            with self.model as Model:
                for reaction in gene.reactions:
                    reaction.knock_out()

                associated_ids = [i.id for i in gene.reactions].copy()

                Model.optimize()
                value2 = Model.objective.value
                percent = ((value2 - self.v1) / abs(self.v1)) * 100
                list_value_opt.append((", ".join(associated_ids), percent))

                # print('%s blocked (bounds: %s), new growth rate %f' %
                #       (gene.id, str([Model.reactions.get_by_id(i.id).bounds for i in gene.reactions]),
                #        Model.objective.value))

        return list_value_opt


if __name__ == "__main__":
    """
    Тестовая модель
    """

    theFileWithModel = "model.json"

    FBA_test = FBA(theFileWithModel)
    list_value_opt = FBA_test.algoritm()

    data_type = [("gene_name", "U1000"), ("percent", float)]
    vdv = np.array(list_value_opt, dtype=data_type)
    list_value_opt = np.sort(vdv, order="percent")[::-1]
    # print(list_value_opt)
    for i in list_value_opt:
        print(f"{i[0]}: {i[1]}%")
