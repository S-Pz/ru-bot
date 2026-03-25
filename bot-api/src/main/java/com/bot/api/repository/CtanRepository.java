package com.bot.api.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.bot.api.entity.Ctan;

import java.time.LocalDate;
import java.util.Optional;

public interface CtanRepository extends JpaRepository<Ctan, Long>{
    Optional<Ctan> findByDataAndHorario(LocalDate data, String horario);

    Optional<Ctan> findByData(LocalDate data);
}
