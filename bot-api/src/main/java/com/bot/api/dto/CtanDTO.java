package com.bot.api.dto;

import java.time.LocalDate;
import java.util.Map;

import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonFormat;

public class CtanDTO {
    
    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate data; 
    
    private String diaDaSemana;
    
    private String horario;
    private Map<String, String> map;

    public CtanDTO (){

    }

    public LocalDate getData(){
        return data;
    }

    public void setData(LocalDate data){
        this.data = data;
    }

    public String getDiaDaSemana(){
        return diaDaSemana;
    }
    
    public void setDiaDaSemana(String diaDaSemana){
        this.diaDaSemana = diaDaSemana;
    }

    public String getHorario(){
        return this.horario;
    }
    
    public Map<String, String> getMap(){
        return map;
    }

   @JsonAnySetter
    public void setMap(String chave, Map<String, String> valor) {
        this.horario = chave;
        this.map = valor;      
    }
}
