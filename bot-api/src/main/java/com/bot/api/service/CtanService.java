package com.bot.api.service;

import com.bot.api.entity.Ctan;
import com.bot.api.repository.CtanRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;
@Service
public class CtanService {
   
    private final CtanRepository repository;

    public CtanService(CtanRepository ctanRepository){
        this.repository = ctanRepository;
    }

    public Ctan findByDataAndHorario (LocalDate data, String horario){
        
        return repository.findByDataAndHorario(data, horario)
            .orElseThrow(()-> new RuntimeException ("Nenhuma data e horário encontrado."));
    }

    public Ctan findByData (LocalDate data){
        
        return repository.findByData(data)
            .orElseThrow(()-> new RuntimeException ("Nenhuma data encontrada."));
    }

    public List<Ctan> crate (List<Ctan> ctan){

        return repository.saveAll(ctan);
    }
}