package com.bot.api.service;

import com.bot.api.dto.CtanDTO;
import com.bot.api.entity.Ctan;
import com.bot.api.repository.CtanRepository;

import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

@Service
public class CtanService {
   
    private final CtanRepository repository;

    public CtanService(CtanRepository ctanRepository){
        this.repository = ctanRepository;
    }

    public Ctan findByHorarioAndData (String horario, LocalDate date){
        
        return repository.findById_DataAndId_Horario(date, horario)
            .orElseThrow(()-> new RuntimeException ("Nada encontrado para a data e horário."));
    }

    // public List<Ctan> findByDataAndHorario (LocalDate data, String horario){
        
    //     List<Ctan> result = repository.findByDataAndHorario(data, horario);
        
    //     if (result.isEmpty()){
    //         throw new RuntimeException("Nenhum dado encontrado para a data e hora");
    //     }

    //     return result;
    // }

    public List<Ctan> findByData (LocalDate date){
        
        List<Ctan> result = repository.findById_Data(date);

        if (result.isEmpty()){
           throw new RuntimeException("Nenhuma data encontrada."); 
        }

        return result;
    }

    public List<Ctan> crate (List<CtanDTO> ctanDto){
        
        if (!ctanDto.isEmpty()){
            
            List<Ctan> list = new ArrayList<>();
    
            for (CtanDTO ctan : ctanDto) {
                list.add(new Ctan(ctan));
            }
            
            return repository.saveAll(list);

        } else {
            
            throw new RuntimeException("Não foi possível salvar, lista vazia.");
        }
    }
}