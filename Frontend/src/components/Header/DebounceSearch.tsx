import { IUserSearch } from "@/models/IUserSearch";
import { getUserSearch } from "@/services/getUserSearch";
import React, { useState, useEffect, ChangeEvent } from "react";
import { Link } from "react-router-dom";

export const DebounceSearch: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState<string>("");
  const [debouncedSearchTerm, setDebouncedSearchTerm] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [searchResults, setSearchResults] = useState<IUserSearch[]>([]);

  useEffect(() => {
    const delay = 500;

    const debounceTimer = setTimeout(() => {
      setDebouncedSearchTerm(searchTerm);
    }, delay);

    return () => {
      clearTimeout(debounceTimer);
    };
  }, [searchTerm]);

  useEffect(() => {
    if (debouncedSearchTerm) {
      fetchSearchResults(debouncedSearchTerm);
    } else {
      setSearchResults([]);
    }
  }, [debouncedSearchTerm]);

  const fetchSearchResults = async (searchTerm: string) => {
    try {
      setIsLoading(true);
      const data = await getUserSearch(searchTerm);
      console.log(data);
      setSearchResults(data);
      setIsLoading(false);
    } catch (error) {
      setIsLoading(false);
    }
  };

  const handleSearch = (event: ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        className="header__input"
        onChange={handleSearch}
      />
      {isLoading ? (
        <ul className="header__loading">Загрузка...</ul>
      ) : (
        <ul className="header__ul_search">
          {searchResults.map((result) => (
            <Link className="header__li_search" to={`/${result.login}`}>
              {result.profileImageUrl ? (
                <img
                  src={`${result.profileImageUrl}`}
                  alt="a"
                  className="header__ava_search"
                />
              ) : (
                <img
                  src={`/img/NoUserPhoto.svg`}
                  alt="a"
                  className="header__ava_search"
                />
              )}
              <span className="header__link_search">{result.login}</span>
            </Link>
          ))}
        </ul>
      )}
    </div>
  );
};
