FROM mcr.microsoft.com/dotnet/sdk:6.0 as build
WORKDIR /src
COPY AskMe.sln .
COPY AskMe.WebApi/*.csproj ./AskMe.WebApi/
COPY AskMe.Core/*.csproj ./AskMe.Core/
COPY AskMe.Service/*.csproj ./AskMe.Service/
COPY . .

RUN dotnet restore && \
    dotnet build -c Debug -o /publish ./AskMe.WebApi && \
    dotnet build -c Debug -o /publish && \
    dotnet build -c Debug -o /publish ./AskMe.Service

FROM build as publish
WORKDIR /src
RUN dotnet publish -c Debug -o /publish

FROM mcr.microsoft.com/dotnet/aspnet:6.0 as final
WORKDIR /publish
COPY --from=publish /publish .
EXPOSE 80

ENTRYPOINT ["dotnet", "AskMe.WebApi.dll"]