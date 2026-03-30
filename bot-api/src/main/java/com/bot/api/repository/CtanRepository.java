package com.bot.api.repository;

import com.bot.api.entity.Ctan;

import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDate;

import java.util.List;
import java.util.Optional;

public interface CtanRepository extends JpaRepository<Ctan, Long>{
    
    Optional<Ctan> findByHorarioAndData(String horario, LocalDate data);

    //List <Ctan> findByDataAndHorario(LocalDate data, String horario);

    List<Ctan> findByData(LocalDate data);
}
