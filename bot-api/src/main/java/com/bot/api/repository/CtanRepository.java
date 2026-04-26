package com.bot.api.repository;

import com.bot.api.entity.Ctan;
import com.bot.api.entity.CtanKey;

import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDate;

import java.util.List;
import java.util.Optional;

public interface CtanRepository extends JpaRepository<Ctan, CtanKey>{
    
    Optional<Ctan> findById_DataAndId_Horario(LocalDate data, String horario);

    //List <Ctan> findByDataAndHorario(LocalDate data, String horario);

    List<Ctan> findById_Data(LocalDate date);
}
