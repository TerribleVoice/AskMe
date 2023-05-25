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
    const delay = 500; // Adjust the debounce delay as needed

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
      setSearchResults(data);
      setIsLoading(false);
    } catch (error) {
      // Handle error
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
        <ul style={{position: "relative", top: "20px"}}>Loading...</ul>
      ) : (
        <ul>
          {searchResults.map((result) => (
            <li style={{position: "relative", top: "20px"}} key={result.login}>
              <Link to={`/${result.login}`}>{result.login}</Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};
