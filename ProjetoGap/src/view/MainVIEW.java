/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package view;

import ctr.IngredienteCTR;
import dto.IngredienteDTO;
import javax.swing.JOptionPane;

/**
 *
 * @author jotavio
 */
public class MainVIEW {

    public static void main(String[] args) {
        int opc = 0;
        IngredienteDTO ingredienteDTO = new IngredienteDTO();
        IngredienteCTR ingredienteCTR = new IngredienteCTR();
        do {
            opc = Integer.parseInt(JOptionPane.showInputDialog("Informe o que deseja fazer:"
                    + "\n1 - Adicionar algo"
                    + "\n2 - Remover algo"
                    + "\n3 - Atualizar algo"
                    + "\n4 - Consultar algo"
                    + "\n0 - SAIR"));
            int classe = 0;
            switch (opc) {
                case 1:
                    classe = Integer.parseInt(JOptionPane.showInputDialog("Informe Qual classe deseja adicionar:"
                            + "\n1- Ingrediente"
                            + "\n2- Receita"
                            + "\n3- Uso"));
                    switch (classe) {
                        case 1:
                            ingredienteDTO.setNome_ingrediente(JOptionPane.showInputDialog("Informe o Nome do Ingrediente:"));
                            JOptionPane.showMessageDialog(null,ingredienteCTR.criaIngrediente(ingredienteDTO));
                            break;
                        default:
                            JOptionPane.showMessageDialog(null, "Erro!");
                    }
            }
        } while (opc != 0);
    }
}
