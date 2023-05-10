import { Outlet } from 'react-router-dom'
import { Header } from './header/Header'
import { ScrollUp } from './scroll/scrollUp'

export const Layout = () => {
  return (
    <>
      <Header />
      <Outlet />
      <ScrollUp />
    </>
  )
}