/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ctr;

import dto.IngredienteDTO;

/**
 *
 * @author jotavio
 */
public class IngredienteCTR {

    public IngredienteDTO[] vetor = new IngredienteDTO[20];
    private int qtd = 0;

    public String criaIngrediente(IngredienteDTO ingredienteDTO) {
        try {
            vetor[qtd] = ingredienteDTO;
            qtd++;
            return "Ingrediente inserido com Sucesso!";
        } catch (Exception e) {
            return "Erro: " + e.getMessage();
        }
    }
    public String atualizaIngrediente(IngredienteDTO ingredienteDTO) {
        try {
            vetor[ingredienteDTO.getId_ingrediente()] = ingredienteDTO;
            return "Ingrediente atualizado com Sucesso!";
        } catch (Exception e) {
            return "Erro: " + e.getMessage();
        }
    }
    public String removeIngrediente(IngredienteDTO ingredienteDTO) {
        try {
            vetor[ingredienteDTO.getId_ingrediente()] = null;
            return "Ingrediente removido com Sucesso!";
        } catch (Exception e) {
            return "Erro: " + e.getMessage();
        }
    }
}