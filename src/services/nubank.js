import createNuBank from 'nubank'

export async function getTransactions() {
  console.log("run service")
  const NuBank = createNuBank()

  try {
    await NuBank.getLoginToken({
      password: process.env.PASSWORD,
      login: process.env.CPF,
    }) // just need to call this once
  } catch (error) {
    console.error(error)
    return error
  }
  console.log("im in")

  const history = await NuBank.getWholeFeed()
  console.log("after history")
  return history
}
