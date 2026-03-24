package com.bot.api.entity;

import java.time.LocalDate;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "ru_ctans")
public class Ctan {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDate data;
    private String diaDaSemana;
    private String horario;
    private String pratoPricipal;
    private String vegetariano;
    private String guarnicao;
    private String salada1;
    private String salada2;
    private String feijao;
    private String suco;
    private String sobremesa;

    public Long getId(){
        return id;
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
    
    public String getHorario (){
        return horario;
    }

    public void setHorario (String horario){
        this.horario = horario;
    }

    public String getPratoPricipal (){
        return pratoPricipal;
    }
    
    public void setPratoPricipal (String pratoPricipal){
        this.pratoPricipal = pratoPricipal;
    }

    public String getVegetariano (){
        return vegetariano;
    }
    
    public void setVegetariano (String vegetariano){
        this.vegetariano = vegetariano;
    }

    public String getGuarnicao (){
        return guarnicao;
    }
    
    public void setGuarnicao(String guarnicao){
        this.guarnicao = guarnicao;
    }

    public String getSalada1 (){
        return salada1;
    }
    
    public void setSalada1(String salada1){
        this.salada1 = salada1;
    }

    public String getSalada2 (){
        return salada2;
    }
    
    public void setSalada2(String salada2){
        this.salada2 = salada2;
    }

    public String getFeijao (){
        return feijao;
    }
    
    public void setFeijao(String feijao){
        this.feijao = feijao;
    }

    public String getSuco (){
        return suco;
    }

    public void setSuco(String suco){
        this.suco = suco;
    }

    public String getSobremesa (){
        return sobremesa;
    }

    public void setSobremesa(String sobremesa){
        this.sobremesa = sobremesa;
    }
}
